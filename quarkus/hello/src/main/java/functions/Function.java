package functions;

import io.quarkus.funqy.Funq;

/**
 * Your Function class
 */
public class Function {

    /**
     * Use the Quarkus Funqy extension for our function. This function simply echoes its input
     * @param input a Java bean
     * @return a Java bean
     */
    @Funq
    public Output function(Input input) {
				
        // Add business logic here

				// NOTE: Use input to capture incoming request data (input.getMessage)
				// return new Output(input.getMessage());
        return new Output("Hello Quarkus World!");
    }

}
