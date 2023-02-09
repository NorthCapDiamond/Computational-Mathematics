package org.demetrius.Commands;

import org.demetrius.util.Environment;

public class RemoveById implements ICommand{
    @Override
    public void execute(Environment environment, String message) {
        int idx;
        try{
            idx = Integer.parseInt(message);
        }catch (Exception e){
            environment.getPrintStream().println("You must type an integer. Command finished");
            return;
        }

        if (idx > environment.getCollectionManager().length()){
            environment.getPrintStream().println("There is no such element");
            return;
        }
        for (int i = idx+1; i <environment.getCollectionManager().length()+1 ; i++) {
            environment.getCollectionManager().findById(i).setId(i-1);
        }
        environment.getCollectionManager().removeById(idx);
        environment.getPrintStream().println("Command finished successfully");

    }

    @Override
    public String getName() {
        return "remove_by_id";
    }

    @Override
    public String getDescription() {
        return "remove_by_id id : Remove an element from the collection by its id.";
    }
}


