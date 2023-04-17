import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pytube import YouTube, Playlist

class Downloader(QDialog):
    def __init__(self, parent=None):
        super(Downloader, self).__init__(parent)

        self.setStyleSheet("background-color:#F0ECE3;")

        self.urlLabel = QLabel('YouTube URL:')
        self.urtwolLabel = QLabel('PlayList URL:')
        self.urthreelLabel = QLabel('Download Location:')

        self.urlEdit = QLineEdit()
        self.urtwolEdit = QLineEdit()
        self.urthreelEdit = QLineEdit()

        self.showMenuButton = QPushButton('Download')

        self.BrowseButton = QPushButton('Browse')


        layout = QGridLayout()
        layout.addWidget(self.urlLabel, 0, 0)
        layout.addWidget(self.urtwolLabel, 1, 0)
        layout.addWidget(self.urthreelLabel, 2, 0)

        layout.addWidget(self.urlEdit, 0, 1)
        layout.addWidget(self.urtwolEdit, 1, 1)
        layout.addWidget(self.urthreelEdit, 2, 1)

        layout.addWidget(self.BrowseButton, 2, 2)

        layout.addWidget(self.showMenuButton, 3,0)
        


        
        self.setLayout(layout)
        self.setWindowTitle('MOHAMED ELSAYED')

        self.BrowseButton.clicked.connect(self.Browse)
        self.showMenuButton.clicked.connect(self.showMenuDialog)
        self.videoQualityComboBox = QComboBox()
        self.videoQualityComboBoxx = QComboBox()

        self.videoQualityComboBox.addItems(['Highest', '1080p', '720p', '480p', '360p', '240p', '144p'])
        self.videoQualityComboBoxx.addItems(['Highest', '1080p', '720p', '480p', '360p', '240p', '144p'])


        self.BrowseButton.setFixedSize(100, 25)
        self.showMenuButton.setFixedSize(150,25)
        self.urlEdit.setFixedSize(150, 25)
        self.urtwolEdit.setFixedSize(150, 25)
        self.urthreelEdit.setFixedSize(150, 25)






        button_style = """
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size:11px;
                border: 2px solid #f44336;
                font-weight:bold;
            }

            QPushButton:hover {
                background-color: white;
                color:#f44336;
            }
        """

        label_style = """
            QLabel {
                font-size:13px;
                font-weight:bold;
                color:black;
            }
    """
        edit_style ="""
            QLineEdit{
                background-color:white;
                border: 2px solid #f44336;
            }
    """

        self.BrowseButton.setStyleSheet(button_style)
        self.showMenuButton.setStyleSheet(button_style)
        
        
        self.urlLabel.setStyleSheet(label_style)
        self.urtwolLabel.setStyleSheet(label_style)
        self.urthreelLabel.setStyleSheet(label_style)

        
        self.urlEdit.setStyleSheet(edit_style)
        self.urtwolEdit.setStyleSheet(edit_style)
        self.urthreelEdit.setStyleSheet(edit_style)
        self.download_Folder = ''
            
    def download(self):
        url = self.urlEdit.text()
        yt = YouTube(url)
        video_quality = self.videoQualityComboBox.currentText()
        if video_quality == 'Highest':
            stream = yt.streams.get_highest_resolution()
        elif video_quality == '1080p':
            stream = yt.streams.filter(res='1080p').first()
        elif video_quality == '720p':
            stream = yt.streams.filter(res='720p').first()
        elif video_quality == '480p':
            stream = yt.streams.filter(res='480p').first()
        elif video_quality == '360p':
            stream = yt.streams.filter(res='360p').first()
        elif video_quality == '240p':
            stream = yt.streams.filter(res='240p').first()
        elif video_quality == '144p':
            stream = yt.streams.filter(res='144p').first()
        else:
            QMessageBox.warning(self, "Error", "Invalid quality option")
            return
        if self.download_Folder:
            stream.download(output_path=self.download_Folder)
            QMessageBox.information(self, "Download Completed", "Download has been completed successfully!")
        else:
            QMessageBox.warning(self, "Error", "Please select download location before download starts")

    def downloadPlaylist(self):
        playlist_url = self.urtwolEdit.text()
        playlist = Playlist(playlist_url)
        videos = playlist.video_urls
        video_quality = self.videoQualityComboBoxx.currentText()
        for video_url in videos:
                yt = YouTube(video_url)
                if video_quality == 'Highest':
                    stream = yt.streams.get_highest_resolution()
                elif video_quality == '1080p':
                    stream = yt.streams.filter(res='1080p').first()
                elif video_quality == '720p':
                    stream = yt.streams.filter(res='720p').first()
                elif video_quality == '480p':
                    stream = yt.streams.filter(res='480p').first()
                elif video_quality == '360p':
                    stream = yt.streams.filter(res='360p').first()
                elif video_quality == '240p':
                    stream = yt.streams.filter(res='240p').first()
                elif video_quality == '144p':
                    stream = yt.streams.filter(res='144p').first()
                else:
                    QMessageBox.warning(self, "Error", "Invalid quality option")
                    return
                if self.download_Folder:
                    stream.download(output_path=self.download_Folder)
        QMessageBox.information(self, "Download Completed", "Download has been completed successfully!")
                

    def downloader(self):
        url = self.urlEdit.text()
        yt = YouTube(url)
        stream = yt.streams.get_by_itag(251)
        if self.download_Folder:
            stream.download(output_path=self.download_Folder)
            QMessageBox.information(self, "Download Completed", "Download has been completed successfully!")
        else:
            QMessageBox.warning(self, "Error", "Please select download location before download starts")



    def Browse(self):
        global download_Path
        download_Path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.urthreelEdit.setText(download_Path)
        self.download_Folder = download_Path


    def showMenuDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Menu')

        videoButton = QPushButton('Download Video (mp4)')
        audioButton = QPushButton('Download Audio (mp3)')
        playlistButton = QPushButton('Download Playlist')

        self.videoQualityComboBox = QComboBox()
        self.videoQualityComboBox.addItems(['Highest', '1080p', '720p', '480p', '360p', '240p', '144p'])

        
        self.videoQualityComboBoxx = QComboBox()
        self.videoQualityComboBoxx.addItems(['Highest', '1080p', '720p', '480p', '360p', '240p', '144p'])


        layout = QVBoxLayout()
        layout.addWidget(videoButton)
        layout.addWidget(self.videoQualityComboBox)
        layout.addWidget(audioButton)
        layout.addWidget(playlistButton)
        layout.addWidget(self.videoQualityComboBoxx)

        dialog.setLayout(layout)

        videoButton.clicked.connect(self.download)
        audioButton.clicked.connect(self.downloader)
        playlistButton.clicked.connect(self.downloadPlaylist)




        button_d = """
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size:11px;
                border: 2px solid #f44336;
                font-weight:bold;
            }

            QPushButton:hover {
                background-color: white;
                color:#f44336;
            }
        """
        button_c = """
            QComboBox {
                background-color: white; 
                color: black; 
                border: 2px solid #008CBA;
                font-weight:bold;

            }

            QComboBox:hover {
                color: white;
                background-color: #008CBA;
                font-weight:bold;
            }
        """



        videoButton.setStyleSheet(button_d)

        audioButton.setStyleSheet(button_d)

        playlistButton.setStyleSheet(button_d)

        self.videoQualityComboBoxx.setStyleSheet(button_c)
        self.videoQualityComboBox.setStyleSheet(button_c)



        videoButton.setFixedSize(150,25)
        audioButton.setFixedSize(150,25)
        playlistButton.setFixedSize(150,25)
        self.videoQualityComboBox.setFixedSize(140,25)
        self.videoQualityComboBoxx.setFixedSize(140,25)




    
        dialog.exec_()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    downloader = Downloader()
    downloader.show()
    downloader.setWindowOpacity(0.9)
    sys.exit(app.exec_())
