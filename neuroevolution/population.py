import tensorflow as tf


class Population:
    """
    ToDo
    """
    def __init__(self):
        """
        ToDo
        """
        self.logger = tf.get_logger()

        self.genome_list = []
        self.initialized_flag = False

    def create_initial_population(self, pop_size, create_genome_function):
        """
        ToDo
        :param pop_size:
        :param create_genome_function
        :return:
        """
        for i in range(pop_size):
            genome = create_genome_function()
            genome.set_id(i)
            self.genome_list.append(genome)

        self.initialized_flag = True
        self.logger.debug("Created genomes: {}\tExample Genome: {}".format(len(self.genome_list), self.genome_list[0]))

    def get_best_genome(self):
        """
        ToDo
        :return:
        """
        return max(self.genome_list, key=lambda x: x.fitness)

    def save_population(self):
        """
        ToDo
        :return:
        """
        raise NotImplementedError("save_population() not yet implemented")

    def load_population(self):
        """
        ToDo
        :return:
        """
        raise NotImplementedError("load_population() not yet implemented")
