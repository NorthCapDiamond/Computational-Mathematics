package org.demetrius.Data;

public class Matrix {
    private double[][] matrix;
    private int id;

    public Matrix(int id){
        this.id = id;
    }
    public Matrix(int id, double[][] matrix){
        this.matrix = matrix;
        this.id = id;
    }

    public double[][] getMatrix() {
        return matrix;
    }

    public void setMatrix(double[][] matrix) {
        this.matrix = matrix;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public void swapLines(int line1, int line2){
        if(this.matrix.length<Math.max(line1, line2)){
            throw new IndexOutOfBoundsException();
        }
        else {
            double[] tmp;
            tmp = matrix[line1];
            matrix[line1] = matrix[line2];
            matrix[line2] = tmp;
        }
        return;
    }
    public int length(){
        return this.matrix.length;
    }

    @Override
    public String toString() {
        String answer = "";
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (j== matrix[i].length-1){
                    answer+="| "+matrix[i][j];
                }
                else {
                    answer += String.format("%.3f",matrix[i][j]) + "\t\t";
                }
            }
            answer+='\n';
        }
        return answer;
    }
}
