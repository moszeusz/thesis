function [ output_args ] = audio_proc(filename)
% audio processing function

% load 'sample'
% filename = 'sample2.mp3';
% audiowrite(filename,y,Fs);

% command = 'cd /home/moszeusz/django/simulator/media';
% [status,cmdout] = system(command)

% samples = [1, 20*Fs];
% [y, Fs] = audioread(filename, samples);

f_max_human = 20000;
f_max_dog = 45000;

% [y2, b] = resample(y,f_max_dog,f_max_human); % upsampling with an interpolation of values
% b; % coefficients of the FIR filter applied to y during the resampling
% figure(1)
% freqz(b)

% x1 = filter(b1,1,y);
% x2 = filter(b2,1,y);

% sound(y2, 2*Fs);
% p1 = audioplayer(x1, Fs)
% p2 = audioplayer(x2, Fs)
% play(p)

% y_length = length(y);
% n = pow2(nextpow2(y_length));
% Y = fft(y,n);
% Y = fft(y);
% y_temp = ifft(Y);
% [Y] = resample(Y,f_max_dog,f_max_human);
% y = ifft(Y);
% p = audioplayer(y, Fs)

% dt = 1/Fs;
% t = 0:dt:20-dt; % first 20 seconds of signal
% N = length(t); % number of samples in one second of signal
% df = Fs/N;
% f = 0:df:Fs-df;

% YY = (2/N)*abs(Y);
% YY = abs(Y);

% f1 = f(4000000:4410000);
% YY1 = YY(4000000:4410000);

% figure(2)
% plot(0:dt:1-dt, y(1:Fs), '+r', 0:dt/2:(2*Fs-1)*dt/2, y2(1:2*Fs), 'ob')  % plot first second of signal
% title('First second of signal resampled by 2')
% xlabel('Time [s]')
% ylabel('Audio signal')
% legend('Original signal','Resampled', ...
%     'Location','NorthWest')
% 
% % dt = 1/2.25*Fs;
% figure(3)
% plot(0:dt:(Fs-1)*dt, y(1:Fs), '+r', 0:dt:(2.25*Fs-1)*dt, y2(1:2.25*Fs), 'og')  % plot first second of signal
% title('First seconds of signal resampled by 2.25 with same time resolution as orignal signal')
% xlabel('Time [s]')
% ylabel('Audio signal')
% legend('Original signal','Resampled', ...
%     'Location','NorthWest')
% 
% figure(4)
% stem(f, YY);
% xlabel('frequency [Hz]');
% grid on;


%% equalizer

% command = '/home/moszeusz/Pobrane/ffmpeg-git-20180208-64bit-static/ffmpeg -y -i sample2.mp3 -af equalizer=f=60:width_type=o:width=1:g=-21.75,equalizer=f=120:width_type=o:width=1:g=-17.2,equalizer=f=240:width_type=o:width=1:g=-13,equalizer=f=480:width_type=o:width=1:g=-13.8,equalizer=f=1000:width_type=o:width=1:g=-8.8,equalizer=f=2000:width_type=o:width=1:g=-5.4,equalizer=f=4000:width_type=o:width=1:g=-6,equalizer=f=8000:width_type=o:width=1:g=10.8,equalizer=f=16000:width_type=o:width=1:g=9.2 output.mp3';
% c1 = '/home/moszeusz/Pobrane/ffmpeg-git-20180208-64bit-static/ffmpeg -y -i ';
% c2 = filename;  % plik, na ktorym sa wykonywane operacje
% c3 = ' -af equalizer=f=60:width_type=o:width=1:g=-21.75,';
% c4 = 'equalizer=f=120:width_type=o:width=1:g=-17.2,';
% c5 = 'equalizer=f=240:width_type=o:width=1:g=-13,';
% c6 = 'equalizer=f=480:width_type=o:width=1:g=-13.8,';
% c7 = 'equalizer=f=1000:width_type=o:width=1:g=-8.8,';
% c8 = 'equalizer=f=2000:width_type=o:width=1:g=-5.4,';
% c9 = 'equalizer=f=4000:width_type=o:width=1:g=-6,';
% c10 = 'equalizer=f=8000:width_type=o:width=1:g=10.8,';
% c11 = 'equalizer=f=16000:width_type=o:width=1:g=9.2 output.mp3';

% command = [c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11];
% [status,cmdout] = system(command)


%% time domain change

% [y, Fs] = audioread(filename);
% command = '/home/moszeusz/Pobrane/ffmpeg-git-20180208-64bit-static/ffmpeg -y -i sample.mp3 -af asetrate=r=30000 output2.mp3';
% c1 = '/home/moszeusz/Pobrane/ffmpeg-git-20180208-64bit-static/ffmpeg -y -i';
% c2 = ' output.mp3';
% c3 = ' -af asetrate=r=';
% c4 = int2str(Fs*(f_max_human/f_max_dog));
% c5 = ' output2.mp3';

% command = [c1 c2 c3 c4 c5];
% [status,cmdout] = system(command)


%% pitchshifting

c1 = '/home/moszeusz/Pobrane/ffmpeg-git-20180208-64bit-static/ffmpeg -y -i ';
c2 = filename;  % plik, na ktorym sa wykonywane operacje
c3 = ' -af rubberband=pitch=0.5:tempo=1 output2.mp3';

command = [c1 c2 c3];
[status,cmdout] = system(command)


% [y, Fs] = audioread(filename);
% command = '/home/moszeusz/Pobrane/ffmpeg-git-20180208-64bit-static/ffmpeg -y -i sample.mp3 -af asetrate=r=30000 output2.mp3';
% c1 = '/home/moszeusz/Pobrane/ffmpeg-git-20180208-64bit-static/ffmpeg -y -i ';
% c2 = filename;
% c3 = ' -af asetrate=r=';
% c4 = int2str(Fs/2);
% c5 = ' output2.mp3';

% command = [c1 c2 c3 c4 c5];
% [status,cmdout] = system(command)

output_args = 0;