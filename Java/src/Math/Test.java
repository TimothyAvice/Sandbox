package Math;

import java.util.*;
import java.util.Arrays;

class ArrayDemo {
    public static void main(String[] args) {

        // initializing unsorted int array
        double intArr[] = {30.02,20.01,5.09,12.2,55.98};

        // sorting array
        Arrays.sort(intArr);

        // let us print all the elements available in list
        System.out.println("The sorted int array is:");
        for (double number : intArr) {
            System.out.println("Number = " + number);
        }

        // entering the value to be searched
        int searchVal = 1000;

        int retVal = Arrays.binarySearch(intArr,searchVal);

        System.out.println("The index of element 12 is : " + retVal);

    }
}
