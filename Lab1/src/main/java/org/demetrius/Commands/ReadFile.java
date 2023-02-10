package org.demetrius.Commands;

import org.demetrius.Data.Matrix;
import org.demetrius.util.Environment;
import org.demetrius.Exceptions.IncorrectNumberOfArgumentsException;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ReadFile implements ICommand{
    @Override
    public void execute(Environment environment, String message) {
        //String link = "/Users/demetrius/Desktop/Вычмат/file.txt";
        environment.getPrintStream().println("Enter the absolute path for the file!");

        String link = null;
        try {
            link = environment.getBufferedReader().readLine();
        } catch (IOException e) {
            environment.getPrintStream().println("Incorrect input. Command finished");
            return;
        }
        FileReader reader;
        try {
            reader = new FileReader(link);
        } catch (FileNotFoundException e) {
            environment.getPrintStream().println("File not found... Command finished");
            return;
        }
        BufferedReader bufferedReader = new BufferedReader(reader);

        int y;
        try {
            String line = bufferedReader.readLine();
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
            try{
                line = bufferedReader.readLine().split(" ");
                if (line.length!=x){
                    throw new IncorrectNumberOfArgumentsException();
                }
                for (int j = 0; j < x; j++) {
                    matrix[i][j] = Double.parseDouble(line[j]);
                }
            } catch (IncorrectNumberOfArgumentsException incorrectNumberOfArgumentsException) {
                environment.getPrintStream().println("Invalid number of arguments... Command finished");
                return;
            } catch (RuntimeException | IOException e){
                environment.getPrintStream().println("Incorrect input. Command finished");
                return;
            }
        }
        Matrix matrix1 = new Matrix(environment.getCollectionManager().length()+1, matrix);
        environment.getCollectionManager().add(matrix1);
        environment.getPrintStream().println("Finished successfully");



    }

    @Override
    public String getName() {
        return "read_file";
    }

    @Override
    public String getDescription() {
        return "read_file : reads matrix from file";
    }
}
