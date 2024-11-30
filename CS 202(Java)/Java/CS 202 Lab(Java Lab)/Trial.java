import java.io.*;

class Count_Word extends Thread{
    public void run(){
        int word_cnt = 0;
        try(BufferedReader br = new BufferedReader(new FileReader("poem.txt"))){
            String line;
            while(line = br.readLine() != null){
                String [] words = line.split();
                word_cnt += words.length;
            }
            System.out.println("Number of words: " + word_cnt);
        }
        catch (FileNotFoundException e){
            System.out.println(e);
        }
    }

}

class Count_Vowels extends Thread{
    public void run(){
        try(BufferedReader br = new BufferedReader(new FileReader("poem.txt"))){
            int vowel_cnt = 0;

            String ch;
            while (ch = br.read() != -1){
                char c = Character.toLowerCase((char) ch);
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                    vowel_cnt += 1;
                }
            }
            System.out.println("NUmber of vowels: " + vowel_cnt);
        }
        catch (FileNotFoundException e){
            System.out.println(e);
        }
    }
}

public class Demo_Lab11{
    public static void main(String []args){
        Thread word_cnt = new Count_Word();
        Thread vowel_cnt = new Count_Vowels();

        word_cnt.start();
        vowel_cnt.start();
    }
}
