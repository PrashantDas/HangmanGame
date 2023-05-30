from . import hangman_words700, hangman_images
import re

def question_word():
    return hangman_words700.pick_one().upper()
    


made_question_word = question_word()

def display_book():
    return {digit: '_' for digit, letter in zip(range(len(made_question_word)), made_question_word)}

display = display_book()


def show_current_word()->str:
    answer = ''
    for each in display.values():
        answer += each + ' '
    return "The word: " + answer

def show_incorrect_attempts():
    return "Incorrect attempts left: " + str(permitted_attempts - counter)


permitted_attempts = 10
counter = 0
wrong_letters_received = ''
correct_letters_received = ''



def new_game(user_input: str) -> str:
    global made_question_word, display, counter, wrong_letters_received, correct_letters_received
    word_under_testing = made_question_word
    letter = user_input.upper()
    if not letter in word_under_testing:         # case 1 - wrong letter received
        if not letter in wrong_letters_received: # case 1.1 - wrong letter is new
            counter += 1
            if counter == permitted_attempts:    # inserted check of counter, if counter full - exit!
                made_question_word = question_word()
                display = display_book()
                counter = 0
                wrong_letters_received = ''
                correct_letters_received = ''
                return ("Dead!", f"The word was: {word_under_testing}", 'Done !') #f"show current word: {show_current_word()}", f"made word {made_question_word}", f"display word {display}" , f"correct letters {correct_letters_received}",'Done !')
            wrong_letters_received += letter+' '
            output_of_wrong_letter = (hangman_images.show_man(counter), "Ow!, I'll be hanged.", show_current_word(),  "Wrong letters used: "+ wrong_letters_received, show_incorrect_attempts())#, f"correct letters {correct_letters_received}")
        else:                                    # case 1.2 - wrong letter is repeated
            output_of_wrong_letter = (show_current_word(), "Wrong letters used: "+ wrong_letters_received, show_incorrect_attempts())#, f"correct letters {correct_letters_received}")
        return_statement = output_of_wrong_letter
    else:                                        # case 2 - correct letter received
        if not letter in correct_letters_received:# case 2.1 - correct letter is new
            correct_letters_received += letter
            for each in re.finditer(letter, made_question_word):
                index = each.span()[0]
                display[index] = letter
            d1 = [each for each in display.values()]
            part_ready = ''.join(d1)
            if part_ready == made_question_word: # inserted check of spelling fulfilment, if satisfied - exit!
                made_question_word = question_word()
                display = display_book()
                counter = 0
                wrong_letters_received = ''
                correct_letters_received = ''
                return ('You did well!', f"The word was: {word_under_testing}", 'Done !')#f"show current word: {show_current_word()}", f"made word {made_question_word}", f"display word {display}", 'Done !')
            output_of_correct_letter = (show_current_word(),  "Wrong letters used: "+ wrong_letters_received, show_incorrect_attempts())#, f"correct letters {correct_letters_received}")
        else:                                    # case 2.2 - correct letter is repeated
            output_of_correct_letter = (show_current_word(), "Wrong letters used: "+ wrong_letters_received, show_incorrect_attempts())#, f"correct letters {correct_letters_received}")
        return_statement = output_of_correct_letter
    return return_statement # one of the four possible output cases, when terminal condition is not yet achieved



