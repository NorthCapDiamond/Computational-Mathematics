package org.demetrius.Managers;

import org.demetrius.Data.Matrix;

import java.util.LinkedList;

public class CollectionManager {
    LinkedList<Matrix> matrices;
    public CollectionManager(){
        matrices = new LinkedList<Matrix>();
    }
    public CollectionManager(LinkedList<Matrix> matrices){
        this.matrices = matrices;
    }
    public void add(Matrix matrix){
        matrices.add(matrix);
    }

    public LinkedList<Matrix> getMatrices() {
        return matrices;
    }

    public void setMatrices(LinkedList<Matrix> matrices) {
        this.matrices = matrices;
    }

    public void removeAllElements(){
        matrices.clear();
    }

    public Matrix getHead(){
        return matrices.getFirst();
    }

    public Matrix getTail(){
        return matrices.getLast();
    }

    public int length(){
        try{
            return matrices.size();
        } catch (NullPointerException nullPointerException){
            return 0;
        }
    }

    public Matrix findById(int id){
        for(Matrix matrix: matrices){
            if(matrix.getId()==id){
                return matrix;
            }
        }
        return null;
    }
    public boolean existsById(int id){
        return findById(id) != null;
    }

    public void removeById(int id){
        if (existsById(id)) {
            matrices.remove(findById(id));
        }
    }

    public void removeLast(){
        this.matrices.remove(findById(matrices.size()));
    }

    public void replace(int id, double[][] matrix){
        Matrix currentMatrix = findById(id);
        if(currentMatrix!=null){
            currentMatrix.setMatrix(matrix);
        }
    }

    @Override
    public String toString(){
        String answer = "";
        answer+=("Displaying the elements of a collection...\n");
        for (Matrix matrix : matrices) {
            answer+=(String.format("Element with id: %d",matrix.getId())+"\n");
            answer+=matrix.toString()+"\n";
        }
        return answer;
    }
}



