class Solution {
    public int[] getConcatenation(int[] nums) {
        int[]a =  new int[nums.length+nums.length];
        for(int i = 0,n=0; i < a.length;i++){
            if(i<nums.length){
                a[i]=nums[i];
            }
            else{
                a[i]=nums[n++];
            }
        }
        return a;
    }
}
