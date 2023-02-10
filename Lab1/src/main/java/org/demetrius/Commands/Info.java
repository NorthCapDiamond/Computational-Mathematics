package org.demetrius.Commands;

import org.demetrius.util.Environment;

import java.io.IOException;

public class Info implements ICommand{
    @Override
    public void execute(Environment environment, String message) throws IOException {
        environment.getPrintStream().println("Created by Dmitry Drobysh, ISU: 333219, Group: P32082\n" +
                "Firstly, you need to create matrix or matrices. " +
                "After that, you are free to use any commands you want))");
    }

    @Override
    public String getName() {
        return "info";
    }

    @Override
    public String getDescription() {
        return "info : returns main information about this work.";
    }
}






