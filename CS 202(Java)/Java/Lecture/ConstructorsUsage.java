public class ConstructorsUsage {
    int l,b;
    ConstructorsUsage(int l,int b){
        //ConstructorsUsage(l);
        this(l);
        this.b = b;
    }

    ConstructorsUsage(int l){
        this.l = l;
    }
}
