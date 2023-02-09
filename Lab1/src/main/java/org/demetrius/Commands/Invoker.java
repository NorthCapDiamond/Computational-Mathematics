package org.demetrius.Commands;



import org.demetrius.util.Environment;

import java.io.IOException;
import java.util.HashMap;

public class Invoker {
    private Environment environment;
    private HashMap<String, ICommand> commandHashMap = new HashMap<>();

    public Invoker(Environment environment, ICommand[] commands){
        this.environment = environment;
        for (ICommand command:commands) {
            commandHashMap.put(command.getName(), command);
        }
    }
    public void executer(String message) throws IOException {
        if (message.split(" ").length > 1) {
            System.setOut(System.out);
            String[] mem = message.split(" ");
            String messageNext = "";
            for (int i = 0; i < mem.length; i++) {
                if (i > 0 && i != mem.length - 1) {
                    messageNext += mem[i] + " ";
                } else {
                    if (i > 0) {
                        messageNext += mem[i];
                    }
                }
            }
            commandHashMap.get(message.split(" ")[0]).execute(environment, messageNext);
        } else {
            System.setOut(System.out);
            commandHashMap.get(message).execute(environment,"");
        }
    }
}
