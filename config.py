# survey_id should remain unchanged
survey_id = "SV_4TLSPrwNIjymdh3"

# the below variables should be set according to your survey specifications

# this text will appear in each question
ab_question_text = "Which of the following audio clips is more appropriate given the information below? <br><br> "
abc_question_text = "Which of the following audio clips is most appropriate given the information below? <br><br> "

abc_with_ref_question_text = "First listen to the reference directly below by pressing the play button. Next, listen to each of the three candidate samples. You should play the reference before listening to each sample. <br/>Then select the candidate sample that is most prosodically similar to the reference."
mc_question_text= "Are there any errors in this speech sample?"
trs_question_text = "Please type the sentence you hear in this audio sample."
mushra_question_text = "First listen to the reference below. Next, listen to each sample next to a slider. <br/>Then rate on a scale from 0 to 100 how prosodically similar the sample is to the reference. <br> Reference: "
mushra_like_question_text = "First listen to the reference below. Next, listen to each sample next to a slider. <br/>Then rate on a scale from 0 to 100 how prosodically similar the sample is to the reference. <br> Reference: "
mos_question_text = "Listen to this speech sample, then rate the quality of the speech."

# the answer options for multiple choice questions
mc_choice_text = ['Yes', 'No']

# these files should contain the urls to be embedded in questions/choices
# each file should have a filename and url per line, separated by whitespace
ab_file1 = "/Users/atli/Documents/IS23_results/sentences/urls/ab_proposed_urls.txt"
ab_file2 = "/Users/atli/Documents/IS23_results/sentences/urls/ab_vanilla_urls.txt"
abc_file1 = "/Users/atli/Documents/IS23_results/sentences/urls/abc_proposed_urls.txt"
abc_file2 = "/Users/atli/Documents/IS23_results/sentences/urls/abc_vanilla_urls.txt"
abc_file3 = "/Users/atli/Documents/IS23_results/sentences/urls/abc_shuffled_urls.txt"
mc_file = "resources/mc-urls.txt"
trs_file = "resources/trs-urls.txt"
mos_file = "/Users/atli/Documents/IS23_results/sentences/urls/mos_urls.txt"
# mushra filenames should be the same across folders
# audiofile urls should vary only by folder name
# any number of folders can be specified
mushra_files = "resources/mushra-urls.txt"
mushra_root = "https://github.com/atliSig/IS_samples/blob/master/mushra/"
# the hidden reference folder should be included in both mushra_folders and mushra_ref_folder
mushra_folders = ["reference", "unedited","edited","random_ref"]
mushra_ref_folder = "reference"
mushra_like_files = "resources/mushra-urls.txt"
mushra_like_root = "https://github.com/atliSig/IS_samples/blob/master/mushra/"
# the hidden reference folder should be included in both mushra_folders and mushra_ref_folder
mushra_like_folders = ["pabc_cleaned_mini","pabc_cleaned_mini_v2","pabc_cleaned_mini_v3","pabc_cleaned_mini_v4", "pabc_cleaned_mini_v5"]
mushra_like_ref_folder = "ground_truth"

abc_with_ref_files = "resources/abc_with_ref-urls.txt"
abc_with_ref_root = "https://github.com/atliSig/IS_samples/blob/master/abc_with_ref/"
abc_with_ref_folders = ["diff_speaker","shuffle","f0_dtw"]
abc_with_ref_ref_folder = "references"

# axy_files = "resources/axy-urls.txt"
# axy_root = "https://github.com/atliSig/IS_samples/blob/master/speaker_similarity_flat/"
# axy_folders = ["target_speaker", "reference_speaker"]
# axy_ref_folder = "experiment_synths"

# MC questions have sentence text embedded
# this file should have a filename and corresponding sentence string per line
# mc_sentence_file = "resources/sentences.txt"
