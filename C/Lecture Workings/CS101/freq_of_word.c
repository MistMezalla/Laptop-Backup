#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to convert a word to lowercase for case-insensitive comparison
void convertToLowercase(char *word) {
    for (int i = 0; word[i] != '\0'; i++) {
        word[i] = tolower(word[i]);
    }
}

// Function to find the frequency of a target word in a paragraph
int findWordFrequency(char *paragraph, char *targetWord) {
    int frequency = 0;
    char *token;

    // Convert target word to lowercase for case-insensitive comparison
    convertToLowercase(targetWord);

    // Tokenize the paragraph and compare each word with the target word
    token = strtok(paragraph, " ,.?!"); // Assuming words are separated by spaces and punctuation
    while (token != NULL) {
        // Convert the current token to lowercase for case-insensitive comparison
        convertToLowercase(token);

        // Compare the current token with the target word
        if (strcmp(token, targetWord) == 0) {
            frequency++;
        }

        // Get the next token
        token = strtok(NULL, " ,.?!"); // Assuming words are separated by spaces and punctuation
    }

    return frequency;
}

int main() {
    char paragraph[1000];
    char targetWord[50];

    // Input the paragraph
    printf("Enter a paragraph:\n");
    fgets(paragraph, sizeof(paragraph), stdin);

    // Input the target word
    printf("Enter the word to find frequency: ");
    scanf("%s", targetWord);

    // Find and print the frequency of the target word in the paragraph
    int frequency = findWordFrequency(paragraph, targetWord);
    printf("Frequency of '%s' in the paragraph: %d\n", targetWord, frequency);

    return 0;
}
