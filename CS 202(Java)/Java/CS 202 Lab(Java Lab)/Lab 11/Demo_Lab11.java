import java.io.*;

// Thread class to count words in the file
class WordCountThread extends Thread {
    public void run() {
        int wordCount = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("poem.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] words = line.split("\\s+"); // Split by whitespace to count words
                wordCount += words.length;
            }
            System.out.println("Total number of words: " + wordCount);
        } catch (IOException e) {
            System.out.println("Error reading the file: " + e.getMessage());
        }
    }
}

// Thread class to count vowels in the file
class VowelCountThread extends Thread {
    public void run() {
        int vowelCount = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("poem.txt"))) {
            int ch;
            while ((ch = br.read()) != -1) {
                char c = Character.toLowerCase((char) ch);
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    vowelCount++;
                }
            }
            System.out.println("Total number of vowels: " + vowelCount);
        } catch (IOException e) {
            System.out.println("Error reading the file: " + e.getMessage());
        }
    }
}

// Main class to execute both threads
public class Demo_Lab11 {
    public static void main(String[] args) {
        // Creating thread objects
        WordCountThread wordThread = new WordCountThread();
        VowelCountThread vowelThread = new VowelCountThread();

        // Starting the threads
        wordThread.start();
        vowelThread.start();
    }
}

//import java.io.*;
//
//class Count_Word extends Thread{
//    public void run() {
//        int word_cnt = 0;
//        try (BufferedReader br = new BufferedReader(new FileReader("poem.txt"))) {
//            String line;
//            while ((line = br.readLine()) != null) {
//                String[] words = line.split("\\s+");
//                word_cnt += words.length;
//            }
//            System.out.println("Number of words: " + word_cnt);
//        } catch (IOException e) {
//            System.out.println(e.getMessage());
//        }
//    }
//}
//
//class Count_Vowels extends Thread{
//    public void run(){
//        try(BufferedReader br = new BufferedReader(new FileReader("poem.txt"))){
//            int vowel_cnt = 0;
//
//            int ch;
//            while ((ch = br.read()) != -1){
//                char c = Character.toLowerCase((char) ch);
//                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
//                    vowel_cnt += 1;
//                }
//            }
//            System.out.println("NUmber of vowels: " + vowel_cnt);
//        }
//        catch (IOException e){
//            System.out.println(e.getMessage());
//        }
//    }
//}
//
//public class Demo_Lab11{
//    public static void main(String []args){
//        Thread word_cnt = new Count_Word();
//        Thread vowel_cnt = new Count_Vowels();
//
//        word_cnt.start();
//        vowel_cnt.start();
//    }
//}
