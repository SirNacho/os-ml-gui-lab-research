//This c++ script is created by Sir Nacho

#include <cstdlib>
#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main() {
  //loading the pre-trained cascade
  CascadeClassifier faceCascade;
  faceCascade.load("haarcascade_frontalface_default.xml");

  //Opens the camera
  VideoCapture video(0);
  if (!video.isOpened()) {
    cout << "Could not open the camera of the device" << endl;
    return -1;
  }

  //Processing frames from the camera
  while (true) {
    Mat frame;
    video >> frame;
    if (frame.empty()) {break;}

    //convert the frame to grayscale
    Mat grey;
    cvtColor(frame, grey, COLOR_BGR2GRAY);

    //Detect faces in the frame
    vector<Rect> faces;
    faceCascade.detectMultiScale(grey, faces, 1.1, 3, 0, Size(30, 30));

    //Drawing the rectangle around the dected face(s)
    for (const Rect& face : faces) {
      rectangle(frame, face, Scalar(255, 0, 0), 2);
    }

    //Display the frame with detected faces
    imshow("Face Detection Test", frame);

    if (waitKey(1) == 27)
      break;
  }

  return EXIT_SUCCESS;
}
