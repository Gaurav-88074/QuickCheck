class Solution {
    public int distinctPrimeFactors(int[] array) {
        HashSet<Integer> m = new HashSet<Integer>();

        for(int i=0; i<array.length; i++){
            int squareroot =(int) Math.squareroott(array[i]);

            for(int j=2; j<=squareroot; j++){
                if(array[i]%j==0){
                    m.add(j);

                    while(array[i]%j==0){
                        array[i] /= j;
                    }
                }
            }
            if(array[i]>1){
                m.add(array[i]);
            }
        }
        return m.size();
    }
}