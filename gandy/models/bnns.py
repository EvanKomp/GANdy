## imports
import gandy.models.models
import tensorflow as tf

class bnn(gandy.models.models.UncertaintyModel):
    '''
    Implements a Bayesian Neural Network (BNN)
    BNNS place a prior on the weights of the network and apply Bayes rule.
    The object of the Bayesian approach for modeling neural networks is to
    capture the epistemic uncertainty, which is uncertainty about the model
    fitness, due to limited training data.

    The idea is that, instead of learning specific weight (and bias) values
    in the neural network, the Bayesian approach learns weight distributions
    - from which we can sample to produce an output for a given input - to
    encode weight uncertainty.

    Thank you to
    https://keras.io/examples/keras_recipes/bayesian_neural_networks/
    for a guide to implementing a BNN with Keras.
    '''

    def create_model_inputs(self, feature_names):
        '''
        Arguments:
            feature_names - example data to make predictions on
                type == ndarray, list, or dictionary      
        Returns:
            inputs 
                type == dictionary of Keras Input layers
        '''
        # do something like:
        # (from https://keras.io/examples/keras_recipes/bayesian_neural_networks/)
        # inputs = {}
        # for feature_name in feature_names:
        #     inputs[feature_name] = tf.keras.layers.Input(
        #         name=feature_name, shape=(1,), dtype=tf.float32
        #     )
        # return inputs

    def prior(kernel_size, bias_size, dtype=None):
        '''
        Arguments:
            kernel_size
                type == float or int
            bias_size
                type == float or int
        Returns:
            prior model 
                type == Keras sequential model
        '''
        # from keras tutorial:
        # Note: this is hard-coded to be unit normal!
        # n = kernel_size + bias_size
        # prior_model = keras.Sequential(
        #     [
        #         tfp.layers.DistributionLambda(
        #             lambda t: tfp.distributions.MultivariateNormalDiag(
        #                 loc=tf.zeros(n), scale_diag=tf.ones(n)
        #             )
        #         )
        #     ]
        # )
        return prior_model

    # Define variational posterior weight distribution as multivariate Gaussian.
    # Note that the learnable parameters for this distribution are the means,
    # variances, and covariances.
    def posterior(kernel_size, bias_size, dtype=None):
        '''
        Arguments:
            kernel_size
                type == float or int
            bias_size
                type == float or int
        Returns:
            posterior model 
                type == Keras sequential model
        '''
        # n = kernel_size + bias_size
        # posterior_model = keras.Sequential(
        #     [
        #         tfp.layers.VariableLayer(
        #             tfp.layers.MultivariateNormalTriL.params_size(n), dtype=dtype
        #         ),
        #         tfp.layers.MultivariateNormalTriL(n),
        #     ]
        # )
        return posterior_model

    # Since the output of the model is a distribution, rather than a point estimate,
    # we use the negative loglikelihood as our loss function to compute how likely to
    # see the true data (targets) from the estimated distribution produced by the model.
    def negative_loglikelihood(targets, estimated_distribution):
        '''
        Arguments:
            targets - training targets
                type == ndarray
            estimated_distribution - 
                type == function that has a log probability (keras loss e.g.)    
        Returns:
            negative log likelihood  
                type == ndarray
        '''
        # do something like:
        # (from https://keras.io/examples/keras_recipes/bayesian_neural_networks/)
        # return -estimated_distribution.log_prob(targets)


    # overridden method from UncertaintyModel class
    def _build(self, **kwargs): 
        '''
        Construct the model
        '''
        # do something like:
        # (from https://keras.io/examples/keras_recipes/bayesian_neural_networks/)
        # feature_names = **kwargs
        # or default feature_names = np.arange(xshape[0])
        # activation, optimizer, loss, num_hidden_units = **kwargs
        # or default activation = 'relu', optimizer = tf.keras.optimizers.adam
        # num_hidden_units = 2 or from kwargs
        # # making appropriate loss:
        # estimated_distribution = tf.keras.losses.MSE
        # loss = negative_loglikelihood(targets, estimated_distribution)
        # get train_size, i.e., train_size = xshape[0]
        
        # inputs = create_model_inputs()
        # input_values = list(inputs.values())
        # features = tf.keras.layers.concatenate(input_values)
        # features = tf.keras.layers.BatchNormalization()(features)

        # Deterministic BNNs have hidden layer weights using Dense layers.
        # Probabilistic BNNs have hidden layer weights using DenseVariational layers.
        # for units in num_hidden_units:
        #   features = tfp.layers.DenseVariational(
        #         units=units,
        #         make_prior_fn=self.prior, 
        #         make_posterior_fn=self.posterior,
        #         kl_weight=1 / train_size,
        #         activation=activation,
        #     )(features)
        # The output is deterministic: a single point estimate.
        # outputs = layers.Dense(units=1)(features)

        # model = keras.Model(inputs=inputs, outputs=outputs)
        # model.compile(optimizer=optimizer, loss=loss)
        # self.model = model
        return None

    # overridden method from UncertaintyModel class
    def _train(self, Xs, Ys, **kwargs):
        '''
        Trains GAN model on data
        
        Arguments:
            Xs/Ys - training examples/targets
                type == ndarray
            
            **kwargs - keyword arguments to assign non-default training parame-
                ters or pass to nested functions.
        '''

        return losses

    # overridden method from UncertaintyModel class
    def _predict(self, Xs, **kwargs):
        '''        
        Arguments:
            Xs - example data to make predictions on
                type == ndarray
                
            **kwargs - keyword arguments for predicting
                
        Returns:
            predictions - array of predictions of targets with the same length
                as Xs
                type == ndarray
                
            uncertainties - array of prediction uncertainties of targets with 
                the same length as Xs
                type == ndarray
        '''
        # pseudocode

        return predictions, uncertainties