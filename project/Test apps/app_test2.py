from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
import joblib
import xgboost
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pandas as pd
from PyQt5 import Qt


model = joblib.load("projects/my_model/Medische_data_model_Manual_scikitlearn2.pkl")
data = pd.read_csv("projects/my_model/medisch-centrum-randstad.csv")

X = data[["genetic", "BMI", "exercise", "smoking", "alcohol", "sugar"]]
y = data["lifespan"]

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2)


model = RandomForestClassifier()
model.fit(X_train, y_train)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Import the QtCore module
        from PyQt5 import QtCore
        from PyQt5 import QtGui

        # Set the size and position of the main window
        self.setGeometry(100, 100, 450, 600)

        # Set the background color to the specified RGB color code
        self.setStyleSheet("background-color: #444654;")




        # Create the title label and set its text and alignment
        self.title_label = QLabel("Lifometer")
        self.title_label.setStyleSheet("color: white; font: bold 45pt;")  # make the font size large and bold
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)  # align the text to the left

        # Initialize the input fields and labels dictionaries
        self.input_fields = {}
        self.input_labels = {}



        # Add the title label to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)

        # Add the input fields and button to the layout
                # Add the input fields and button to the layout
               # Add the input fields and button to the layout
        fields = ["genetic", "BMI", "exercise", "smoking", "alcohol", "sugar"]
        for i in range(0, len(fields), 3):
            hbox = QHBoxLayout()
            for field in fields[i:i+3]:
                vbox = QVBoxLayout()  # use a vertical layout for each input field and label pair
                hbox_field = QHBoxLayout()  # use a horizontal layout for the label and input field
                self.input_labels[field] = QLabel(field)
                self.input_labels[field].setStyleSheet("color: white;")
                self.input_labels[field].setAlignment(QtCore.Qt.AlignRight)  # align the labels to the left
                hbox_field.addWidget(self.input_labels[field])
                self.input_fields[field] = QLineEdit()
                self.input_fields[field].setFixedWidth(100)
                self.input_fields[field].setStyleSheet("color: white; padding-left: 10px;")  # add left padding to the input field
                self.input_fields[field].setAlignment(QtCore.Qt.AlignLeft)  # align the input fields to the left
                hbox_field.addWidget(self.input_fields[field])
                vbox.addLayout(hbox_field)  # add the horizontal layout to the vertical layout
                hbox.addLayout(vbox)  # add the vertical layout to the horizontal layout
            layout.addLayout(hbox)  # add the horizontal layout to the main layout
        self.predict_button = QPushButton("Predict")
        self.predict_button.setFixedWidth(75)  # make the button shorter
        self.predict_button.setStyleSheet("color: white;")  # set the font color of the button to white
        self.predict_button.clicked.connect(self.make_prediction)
        layout.addWidget(self.predict_button)

        # Create the label to display the prediction and set its font and alignment
        self.prediction_label = QLabel()
        self.prediction_label.setStyleSheet("color: white;")
        self.prediction_label.setFont(QFont("Helvetica", 80, QFont.Bold))
        self.prediction_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.prediction_label)

        # Set the layout for the main window
        self.setLayout(layout)



    def make_prediction(self):
        # Get the input data from the input fields
        input_data = pd.DataFrame(
            data={
                field: [float(self.input_fields[field].text())]
                for field in ["genetic", "BMI", "exercise", "smoking", "alcohol", "sugar"]
            }
        )

        # Use the model to make a prediction
        prediction = model.predict(input_data)[0] 

        # Update the prediction label with the prediction
        self.prediction_label.setText(str(prediction))
    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()