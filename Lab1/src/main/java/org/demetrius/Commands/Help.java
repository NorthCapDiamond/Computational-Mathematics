package org.demetrius.Commands;

import org.demetrius.util.Environment;

public class Help implements ICommand{
    @Override
    public void execute(Environment environment, String message) {
        environment.getPrintStream().println("\nhelp : Display help for available commands.\n" +
                "info : returns main information about this work.\n"+
                "clean : clear the collection.\n" +
                "add : add matrix line by line from input.\n"+
                "read_file : reads matrix from file\n"+
                "exit : exit the program. (without saving to file)\n" +
                "remove_by_id id : Remove an element from the collection by its id.\n" +
                "show : print to standard output all elements of the collection in string representation.\n" +
                "gauss : Calculates the determinant, outputs a triangular matrix, Outputs vectors of unknowns, outputs residual vectors.\n"+
                "rick : NOOOOOOOOOOO!\n"+
                "panic : shut up and go to bed.\n");
    }

    @Override
    public String getName() {
        return "help";
    }

    @Override
    public String getDescription() {
        return "help : Display help for available commands.";
    }
}