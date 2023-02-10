package org.demetrius.Commands;

import org.demetrius.Managers.CollectionManager;
import org.demetrius.util.Environment;

public class Show implements ICommand{

    @Override
    public void execute(Environment environment, String message) {
        CollectionManager collectionManager = environment.getCollectionManager();
        if(collectionManager.length()>0){
            environment.getPrintStream().println(collectionManager.toString());
            environment.getPrintStream().println("Finished successfully");
        }
        else {
            environment.getPrintStream().println("Collection is empty");
        }

    }

    @Override
    public String getName() {
        return "show";
    }

    @Override
    public String getDescription() {
        return "show : print to standard output all elements of the collection in string representation.";
    }
}



