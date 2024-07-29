import docx
from sklearn.feature_extraction.text import CountVectorizer

# Function to read text from a .docx file
def read_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Path to your .docx file - Verify this path is correct!
file_path = r"/content/CVpracticaltest.docx"  # Double-check this path

# Read the text from the file
text = read_docx(file_path)

# Assuming you have your training and testing data
inputs_train = [text]  # Replace with your actual training data
inputs_test = [text]   # Replace with your actual testing data

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the training data
Xtrain = vectorizer.fit_transform(inputs_train)

# Transform the testing data
Xtest = vectorizer.transform(inputs_test)

# Print the vectors
print("Training Data Vector:\n", Xtrain.toarray())
print("Testing Data Vector:\n", Xtest.toarray())
print("Feature Names:\n", vectorizer.get_feature_names_out())