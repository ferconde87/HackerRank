class Calculator{
    int power(int n, int p){
        if(n < 0 || p < 0){
            throw new IllegalArgumentException("n and p should be non-negative");
        }
        return pow(n, p);
    }
    
    int pow(int n, int p){
        int ans = 1;
        int q = p/2;
        for(int i = 0; i < q; i++){
            ans *= n*n;
        }
        if(p%2==1)
            ans *= n;
        return ans;
    }
}