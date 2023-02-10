package org.demetrius.Commands;

import org.demetrius.Data.Matrix;
import org.demetrius.util.Environment;
import org.demetrius.util.SimpleAudioPlayer;

import java.io.IOException;
import java.math.BigDecimal;

public class Gauss implements ICommand {
    @Override
    public void execute(Environment environment, String message) throws IOException {
        Matrix matrix;
        if(environment.getCollectionManager().length()==0){
            environment.getPrintStream().println("create matrix first!");
            return;
        }
        if(environment.getCollectionManager().length()>1){
            environment.getPrintStream().println("Choose matrix by its id");
            int id;
            try {
                id = Integer.parseInt(environment.getBufferedReader().readLine());
                matrix = environment.getCollectionManager().findById(id);
                if(matrix==null){
                    throw new Exception();
                }
            } catch (Exception e){
                environment.getPrintStream().println("incorrect id. Command finished.");
                return;
            }
        }
        else {
            matrix = environment.getCollectionManager().findById(1);
        }
        environment.getPrintStream().println("The original matrix :");
        environment.getPrintStream().println(matrix.toString());
        Matrix originalMatrix;
        double[][] originalMatrixArray = new double[matrix.length()][matrix.length()+1];
        for (int i = 0; i < matrix.length(); i++) {
            for (int j = 0; j < matrix.length()+1; j++) {
                originalMatrixArray[i][j] = matrix.getMatrix()[i][j];
            }
        }
        originalMatrix = new Matrix(1010101, originalMatrixArray);


        /*boolean found = false;

        for (int i = 0; i < matrix.getMatrix().length; i++) {
            if(matrix.getMatrix()[i][i]==0){
                for (int j = i; j < matrix.getMatrix().length; j++) {
                    if (matrix.getMatrix()[j][i]!=0){
                        matrix.swapLines(j, i);
                        found = true;
                    }
                }
                if(!found){
                    for (int j = 0; j < i; j++) {
                        if(matrix.getMatrix()[j][i]!=0 && matrix.getMatrix()[i][j]!=0){
                            found = true;
                            matrix.swapLines(i,j);
                        }
                    }
                    if (!found){
                        environment.getPrintStream().println("enter only joint matrices. Command finished");
                        return;
                    }
                }
            }
        }
        good idea, but it's almost impossible to write effectively!
*/





        double[][] matrixArray = matrix.getMatrix();


        for (int i = 0; i < matrixArray.length; i++) {
            if (matrixArray[i][i]==0){
                for (int j = 0; j < matrixArray.length; j++) {
                    if(matrixArray[j][i]!=0){
                        for (int k = 0; k < matrixArray.length+1; k++) {
                            matrixArray[i][k]+=matrixArray[j][k];
                        }
                        break;
                    }
                }
            }
        }
        matrix = new Matrix(-1,matrixArray);

        environment.getPrintStream().println("Matrix after getting rid of 0 in the main diagonal :");
        environment.getPrintStream().println(matrix.toString());



        //forward stroke

        double c;
        double[] allX = new double[matrixArray.length];
        Matrix matrix1 = new Matrix(0);

        for (int i = 0; i < matrixArray.length; i++) {
            for (int j = i+1; j < matrixArray.length ; j++) {
                if(matrixArray[i][i]==0){
                    for (int k = i; k <matrixArray.length ; k++) {
                        if(matrixArray[k][i]!=0){
                            for (int l = 0; l < matrixArray.length+1; l++) {
                                matrixArray[i][l]+=matrixArray[k][l];
                            }
                        }
                    }
                }
                c = matrixArray[j][i]/matrixArray[i][i];
                for (int k = matrixArray.length; k >=i ; k--) {
                    matrixArray[j][k] -=c*matrixArray[i][k];
                }
            }

            matrix1 = new Matrix(environment.getCollectionManager().length()+1, matrixArray);
            environment.getPrintStream().printf("iteration number : %d\n",i+1 );
            environment.getPrintStream().println(matrix1.toString());
        }

        BigDecimal determinant = BigDecimal.valueOf(1);
        double tmp = 0;
        // finding determinant and creating diagonal of ones
        for (int i = 0; i < matrixArray.length; i++) {
            tmp = matrixArray[i][i];
            determinant = determinant.multiply(BigDecimal.valueOf(tmp));
            for (int j = 0; j < matrix.length()+1; j++) {
                matrixArray[i][j]/=tmp;
            }
        }
        matrix1 = new Matrix(environment.getCollectionManager().length()+1, matrixArray);

        environment.getPrintStream().println("\nTriangular matrix :");
        environment.getPrintStream().println(matrix1.toString());
        environment.getPrintStream().println();
        environment.getPrintStream().println("Determinant :");
        environment.getPrintStream().println(determinant);
        environment.getPrintStream().println();



        //reverse stroke
        allX[matrixArray.length-1] = matrixArray[matrixArray.length-1][matrixArray.length];
        for (int i = matrixArray.length-2; i >=0 ; i--) {
            allX[i] = matrixArray[i][matrixArray.length];
            for (int j = i+1; j < matrixArray.length ; j++) {
                allX[i]-=matrixArray[i][j]*allX[j];
            }
        }
        environment.getPrintStream().println("All X_i values :");
        for (int i = 0; i < matrixArray.length; i++) {
            environment.getPrintStream().printf("X%d = %.3f  ",i+1,allX[i]);
        }
        environment.getPrintStream().println("\n");
        environment.getPrintStream().println("All residual vectors :");


        //residual vectors

        String residualVectors = "";
        double leftPart = 0;
        int counter = 0;
        for (int i = 0; i < originalMatrix.length(); i++) {
            for (int j = 0; j < originalMatrix.length(); j++) {
                leftPart+=allX[j]*originalMatrix.getMatrix()[i][j];
            }
            residualVectors+= String.format("R%d = %.20f  ", i+1, originalMatrix.getMatrix()[i][originalMatrix.length()]-leftPart);
            counter++;
            if(counter==5){
                counter=0;
                residualVectors+="\n";
            }
            leftPart = 0;
        }
        environment.getPrintStream().println(residualVectors);

        //music

        try {
            SimpleAudioPlayer simpleAudioPlayer = new SimpleAudioPlayer("/Users/demetrius/Desktop/Вычмат/Lab1/music/yes.wav");
            simpleAudioPlayer.play();

        }catch (Exception e){
            e.printStackTrace();
            return;
        }

        environment.getPrintStream().println();
        environment.getPrintStream().println("Command finished successfully");

        return;


    }

    @Override
    public String getName() {
        return "gauss";
    }

    @Override
    public String getDescription() {
        return "gauss : Calculates the determinant, outputs a triangular matrix, Outputs vectors of unknowns, outputs residual vectors";
    }
}



/*

1 1 0
0 0 1
1 0 0

1 0 0
0 0 1
1 1 0

1 0 0
1 1 0
0 0 1


1 0 1
0 1 0
1 0 0

А тут надо подумать!

И мы придумали!)))
 */

