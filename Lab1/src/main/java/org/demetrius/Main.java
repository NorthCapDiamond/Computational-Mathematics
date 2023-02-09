package org.demetrius;

import org.demetrius.Commands.*;
import org.demetrius.Managers.CollectionManager;
import org.demetrius.util.Environment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        CollectionManager manager = new CollectionManager();
        ArrayList<String> history = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        PrintStream writer = new PrintStream(System.out);
        Environment environment = new Environment(manager,reader, writer, history);

        Invoker invoker = new Invoker(environment, new ICommand[]{
                new Rick(), new Exit(), new Help(),
                new Show(), new Add(), new ReadFile(),
                new Clean(), new ReadFile(), new Info(),
                new RemoveById(), new Gauss(), new Panic()}
        );
        System.out.println("Hello, welcome to Drobina's program");
        System.out.println("Type 'help' to see commands");
        while(true){
            try {
                String userTyping = reader.readLine();
                invoker.executer(userTyping);
                history.add(userTyping.split(" ")[0]);
            }
            catch (IOException ex){
                System.out.println("Incorrect input");
            }
            catch (NullPointerException exe){
                System.out.println("No such command found");
            }
        }
    }
}

