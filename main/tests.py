import string

from django.conf import settings
from django.test import TestCase

from main.business_rules import _remove_puctuations, word_counter
from main.forms import WordCountForm


class BusinessRulesTests(TestCase):
    # --------------------------------------------------------------------------
    #   Punctuation removal
    # --------------------------------------------------------------------------
    def test_puctuation_removal__without_punctuation(self):
        test_text = 'words without puctuation'
        expected_text = test_text

        self.assertEqual(_remove_puctuations(test_text), expected_text)

    def test_puctuation_removal__with_isolated_punctuation(self):
        test_text = 'words , with @ many ... puctuations !'
        expected_text = 'words  with  many  puctuations '

        self.assertEqual(_remove_puctuations(test_text), expected_text)

    def test_puctuation_removal__with_punctuation_next_to_words(self):
        test_text = 'words, with puctuations next? to the words!'
        expected_text = 'words with puctuations next to the words'

        self.assertEqual(_remove_puctuations(test_text), expected_text)

    def test_puctuation_removal__empty_text(self):
        test_text = ''
        expected_text = test_text

        self.assertEqual(_remove_puctuations(test_text), expected_text)

    def test_puctuation_removal__punctuation_only(self):
        test_text = string.punctuation
        expected_text = ''

        self.assertEqual(_remove_puctuations(test_text), expected_text)

    def test_puctuation_removal__scattered_punctuation_only(self):
        test_text = ' '.join(list(string.punctuation))
        expected_text = ' ' * (len(string.punctuation) - 1)

        self.assertEqual(_remove_puctuations(test_text), expected_text)

    # --------------------------------------------------------------------------
    #   Word counting
    # --------------------------------------------------------------------------
    def test_word_counter__common_case(self):
        test_text = 'these are four words'
        expected_count = 4

        self.assertEqual(word_counter(test_text), expected_count)

    def test_word_counter__with_numbers(self):
        test_text = 'these are 4 words'
        expected_count = 4

        self.assertEqual(word_counter(test_text), expected_count)

    def test_word_counter__with_spurious_spaces(self):
        test_text = '     these     are four    \t\t \n   words \n'
        expected_count = 4

        self.assertEqual(word_counter(test_text), expected_count)

    def test_word_counter__with_punctuation(self):
        test_text = 'these ?! are (four) words .'
        expected_count = 4

        self.assertEqual(word_counter(test_text), expected_count)

    def test_word_counter__empty_text(self):
        test_text = ''
        expected_count = 0

        self.assertEqual(word_counter(test_text), expected_count)

    def test_word_counter__equivalent_to_empty_text(self):
        test_text = '  . % $$$ \t '
        expected_count = 0

        self.assertEqual(word_counter(test_text), expected_count)


class WordCountFormTests(TestCase):
    def test_text__common_case(self):
        test_text = 'These are some words.'
        expected_text = test_text

        form = WordCountForm(data={'text': test_text})

        self.assertEqual(form.errors, {})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['text'], expected_text)

    def test_text__empty_text(self):
        test_text = ''

        form = WordCountForm(data={'text': test_text})

        self.assertEqual(form.errors, {'text': ['This field is required.']})
        self.assertFalse(form.is_valid())

    def test_text__text_size_within_limit(self):
        test_text = 'A' * settings.MAX_TEXT_SIZE
        expected_text = test_text

        form = WordCountForm(data={'text': test_text})

        self.assertEqual(form.errors, {})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['text'], expected_text)

    def test_text__text_size_beyond_limit(self):
        # One more character than the limit
        test_text = 'A' * settings.MAX_TEXT_SIZE + 'B'

        form = WordCountForm(data={'text': test_text})

        self.assertEqual(
            form.errors,
            {
                'text': [
                    f'Ensure this value has at most {settings.MAX_TEXT_SIZE} '
                    f'characters (it has {len(test_text)}).'
                ]
            }
        )
        self.assertFalse(form.is_valid())
