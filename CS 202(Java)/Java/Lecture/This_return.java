public class This_return {
    int l,b;

    This_return(int x,int b){
        l = x;
        this.b = b;
    }

    This_return get_this(){
        return this;
    }
}
