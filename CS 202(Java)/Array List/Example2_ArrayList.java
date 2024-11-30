//Show substring, delete strings with substring (removeIf), upperCase

package MyPackage;

import java.util.*;  

public class Example2{  
	public static void main(String args[]){  
			
			ArrayList<String> list=new ArrayList<String>();//Creating arraylist    
		    
			list.add("Mango");  //Adding object in arraylist    
		    list.add("Apple");    
		    list.add("Babana");    
		    list.add("Mango");
		    
		    System.out.println(list); 
		    
		    //list.removeIf(x->x.substring(1,3).equals("an"));
		    
		    //System.out.println(list); 
		     
		    //list.replaceAll(s->s.toUpperCase());
		    //System.out.println(list); 
		    System.out.println(list.get(0).substring(2,4));
		     
		    /*Iterator itr=list.iterator();//getting the Iterator  
		     
		     while(itr.hasNext()){//check if iterator has the elements  
		      System.out.print(itr.next()+" ");//printing the element and move to next 
		     }*/
		     
		     /*for(String s:list) {
		    	System.out.print(s+" ");
		     }*/
	}
}