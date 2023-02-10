package org.demetrius.Commands;

import org.demetrius.Data.Matrix;
import org.demetrius.util.Environment;
import org.demetrius.Exceptions.IncorrectNumberOfArgumentsException;

import java.io.IOException;

public class Add implements ICommand{
    @Override
    public void execute(Environment environment, String message)  {
        environment.getPrintStream().println("Enter the size of matrix");
        int y;
        try {
            String line = environment.getBufferedReader().readLine();
            y = Integer.parseInt(line);
        }catch (Exception e){
            environment.getPrintStream().println("Incorrect input. Command finished");
            return;
        }
        int x = y+1;
        if(y<=1){
            environment.getPrintStream().println("Are you kidding??????? Command finished");
            return;
        }

        double[][] matrix = new double[y][x];
        String[] line;

        for (int i = 0; i < y; i++) {
            environment.getPrintStream().printf("Enter the line (length = %d). format: \'a1 a2 a3....\'\n", x);
            try{
                line = environment.getBufferedReader().readLine().split(" ");
                if (line.length!=x){
                    throw new IncorrectNumberOfArgumentsException();
                }
                for (int j = 0; j < x; j++) {
                    matrix[i][j] = Double.parseDouble(line[j]);
                }
            } catch (IncorrectNumberOfArgumentsException incorrectNumberOfArgumentsException) {
                environment.getPrintStream().println("Invalid number of arguments...");
                i--;
                continue;
            } catch (RuntimeException | IOException e){
                environment.getPrintStream().println("Incorrect input");
                i--;
                continue;
            }
        }
        Matrix matrix1 = new Matrix(environment.getCollectionManager().length()+1, matrix);
        environment.getCollectionManager().add(matrix1);
        environment.getPrintStream().println("Finished successfully");

    }

    @Override
    public String getName() {
        return "add";
    }

    @Override
    public String getDescription() {
        return "add matrix line by line from input";
    }
}
