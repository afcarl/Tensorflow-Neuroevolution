import tensorflow as tf
from absl import logging

import neuroevolution as ne


def create_test_genome(encoding):
    activation_default = tf.keras.activations.deserialize("tanh")
    activation_out = tf.keras.activations.deserialize("sigmoid")

    gene_list = list()
    gene_list.append(encoding.create_gene_connection(1, 3, 0.5))
    gene_list.append(encoding.create_gene_connection(1, 4, 0.5))
    gene_list.append(encoding.create_gene_connection(2, 3, 0.5))
    gene_list.append(encoding.create_gene_connection(2, 4, 0.5))
    gene_list.append(encoding.create_gene_connection(3, 4, 0.5))
    gene_list.append(encoding.create_gene_node(3, 0.5, activation_default))
    gene_list.append(encoding.create_gene_node(4, 0.5, activation_out))

    genotype = dict()
    for (gene_id, gene) in gene_list:
        genotype[gene_id] = gene

    genome_id, genome = encoding.create_genome(genotype=genotype)
    return genome


def test_xor_wt_environment():
    """
    TODO
    """

    logging.set_verbosity(logging.DEBUG)
    logging.info("Using TF Version {}".format(tf.__version__))
    assert tf.__version__[0] == '2'  # Assert that TF 2.x is used

    config = ne.load_config('./test_config.cfg')
    environment = ne.environments.XORWeightTrainingEnvironment(config)
    encoding = ne.encodings.DirectEncoding(trainable=True, dtype=tf.float32, run_eagerly=False)
    genome = create_test_genome(encoding)

    environment.eval_genome_fitness(genome)
    environment.replay_genome(genome)
    genome.visualize()


if __name__ == '__main__':
    test_xor_wt_environment()
