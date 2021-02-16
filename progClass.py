import tkinter as tk
import tkinter.ttk as bar
from gui import Root

class progCl:

    def __init__(self):
        # ! specializedTQDM handles most of the display details, displayManager is an
        # ! additional bit of calculations to ensure that the specializedTQDM progressbar
        # ! works accurately across downloads from multiple processes
        self.progressBar = bar.Progressbar(Root, orient= tk.HORIZONTAL , mode='determinate')

    def set_song_count_to(self, songCount: int) -> None:
        '''
        `int` `songCount` : number of songs being downloaded
        RETURNS `~`
        sets the size of the progressbar based on the number of songs in the current
        download set
        '''

        # ! all calculations are based of the arbitrary choice that 1 song consists of
        # ! 100 steps/points/iterations
        self.progressBar.configure(length = songCount * 100)

    def notify_download_skip(self) -> None:
        '''
        updates progress bar to reflect a song being skipped
        '''

        self.progressBar.step(100)

    def pytube_progress_hook(self, stream, chunk, bytes_remaining) -> None:
        '''
        Progress hook built according to pytube's documentation. It is called each time
        bytes are read from youtube.
        '''

        # ! This will be called until download is complete, i.e we get an overall
        # ! self.progressBar.update(90)

        fileSize = stream.filesize

        # ! How much of the file was downloaded this iteration scaled put of 90.
        # ! It's scaled to 90 because, the arbitrary division of each songs 100
        # ! iterations is (a) 90 for download (b) 5 for conversion & normalization
        # ! and (c) 5 for ID3 tag embedding
        iterFraction = len(chunk) / fileSize * 90

        self.progressBar.step(iterFraction)

    def notify_conversion_completion(self) -> None:
        '''
        updates progresbar to reflect a audio conversion being completed
        '''

        self.progressBar.step(5)

    def notify_download_completion(self) -> None:
        '''
        updates progresbar to reflect a download being completed
        '''

        # ! Download completion implie ID# tag embedding was just finished
        self.progressBar.step(5)

    def reset(self) -> None:
        '''
        prepare displayManager for a new download set. call
        `displayManager.set_song_count_to` before next set of downloads for accurate
        progressbar.
        '''

        self.progressBar["value"]=0

    #def clear(self) -> None:
        '''
        clear the tqdm progress bar
        '''

        #self.progressBar.clear()

    def close(self) -> None:
        '''
        clean up TQDM
        '''

        self.progressBar.stop()
