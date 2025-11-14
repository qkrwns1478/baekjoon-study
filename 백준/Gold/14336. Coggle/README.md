# [Gold II] Coggle - 14336 

[문제 링크](https://www.acmicpc.net/problem/14336) 

### 성능 요약

메모리: 139024 KB, 시간: 160 ms

### 분류

구현, 자료 구조, 문자열, 정렬, 트리, 이분 탐색, 해시를 사용한 집합과 맵, 백트래킹, 트라이

### 제출 일자

2025년 11월 14일 20:04:58

### 문제 설명

<p>Like everyone else on their vacation, the cows play the cow version of the word game called Boggle: Coggle. It's a similar game where 25 letter dice are rolled into a matrix like this one:</p>

<pre>           Z C C D X
           K Q M N B
           U O W Z Y
           F C O I J
           P A Q Z T
</pre>

<p>Words are made (and thus points scored) by starting at some letter and proceeding to one of its (as many as) eight neighbors, etc. until the successive letters spell out a word from a dictionary</p>

<p>In the matrix above, the lower 'C' can be used to form the words "CAP", "COW", and "COOK" (but not "COD" or "PACK"). The complete list of dictionary words for the above square is: "CAP", "COOK", "COW", "OWN", "WIT", "WOO", "ZOO", and "ZOOM".</p>

<p>Your program should read the dictionary from file dict.txt (which is alphabetized and has fewer than 25,000 words; each word is no longer than 20 characters). The actual dictionary contents can be inspected at <a href="https://d2gd6pc034wcta.cloudfront.net/data/1165.zip">here</a>.</p>

<p>Help Bessie see how good she can do. Read in five rows of five letters that represent the dice and see how many words from the dictionary can be formed. Don't use any given die's letter twice in the same word.</p>

<p>Count the number of words that can be formed (a number that might well be smaller than the number of ways a word a can be formed since words might be formed in more than one way).</p>

### 입력 

 <ul>
	<li>Lines 1..5: Line i contains five space-separated upper-case letters that are row i</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the number of words in the dictionary that can be formed using the described rules</li>
</ul>

