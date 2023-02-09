package org.demetrius.Commands;


import org.demetrius.util.Environment;

import java.io.IOException;

public interface ICommand {
    void execute(Environment environment, String message) throws IOException;
    String getName();
    String getDescription();
}
