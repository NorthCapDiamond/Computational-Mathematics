package org.demetrius.Commands;


import org.demetrius.util.Environment;

public class Exit implements ICommand{

    @Override
    public void execute(Environment environment, String message) {
        environment.getPrintStream().println("You finished the program, goodbye!)");
        System.exit(0);
    }

    @Override
    public String getName() {
        return "exit";
    }

    @Override
    public String getDescription() {
        return "exit : exit the program. (without saving to file)";
    }
}
