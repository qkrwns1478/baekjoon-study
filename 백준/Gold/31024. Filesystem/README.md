# [Gold III] Filesystem - 31024 

[문제 링크](https://www.acmicpc.net/problem/31024) 

### 성능 요약

메모리: 114740 KB, 시간: 148 ms

### 분류

많은 조건 분기, 자료 구조, 해시를 사용한 집합과 맵, 구현, 연결 리스트, 파싱, 재귀, 문자열, 트리, 트리를 사용한 집합과 맵, 집합과 맵

### 제출 일자

2025년 10월 25일 17:40:12

### 문제 설명

<p>Given a series of file system commands and queries, output the contents of the file requested by each query (a query is a filename to be printed out). If the query is invalid (e.g. path does not exist), the text <code>invalid!</code> must be printed.</p>

<p>The following commands must be supported:</p>

<ul>
	<li>
	<dl>
		<dt><code>echo "<content>" > <path></code></dt>
		<dd>
		<p>Writes <code><content></code> to the file <code><path></code>. If <code><path></code> exists, it must be a file, and the contents will be replaced. If the path does not exist, its parent directory must exist, and the file will be created. <code><content></code> will only contain ASCII numbers, letters, <code>*</code>, <code>?</code>, <code><</code>, <code>></code>, and space.</p>
		</dd>
	</dl>
	</li>
	<li>
	<dl>
		<dt><code>cp <source> <destination></code></dt>
		<dd>
		<p>Copies file <code><source></code> to file or directory <code><destination></code>. If <code><destination></code> already exists and is a directory, the file will be copied to the <code><destination></code> directory, with a filename which is the final path component of <code><source></code>. Otherwise, <code><destination></code> is the new filename, and its parent directory must already exist. The new file replaces any existing content.</p>
		</dd>
	</dl>
	</li>
	<li>
	<dl>
		<dt><code>mv <source> <destination></code></dt>
		<dd>
		<p>Moves file or directory <code><source></code> to the file or directory <code><destination></code>. Similarly to <code>cp</code>, if <code><destination></code> already exists and is a directory, the source file/directory will be moved to a path within the <code><destination></code> directory whose name matches the final path component of <code><source></code>. Otherwise, <code><destination></code> is the new filename, and its parent directory must already exist. The new file replaces any existing content, and <code><source></code> is removed.</p>
		</dd>
	</dl>
	</li>
	<li>
	<dl>
		<dt><code>rm <path></code></dt>
		<dd>
		<p>Deletes the file with the path <code><path></code>.</p>
		</dd>
	</dl>
	</li>
	<li>
	<dl>
		<dt><code>mkdir <path></code></dt>
		<dd>
		<p>Creates a directory with the path <code><path></code>. The parent directory must already exist.</p>
		</dd>
	</dl>
	</li>
	<li>
	<dl>
		<dt><code>rmdir <path></code></dt>
		<dd>
		<p>Removes an empty directory with the path <code><path></code>.</p>
		</dd>
	</dl>
	</li>
</ul>

<p>All filesystem paths will only contain numbers, letters, or <code>/</code> and will not exceed 31 characters or 7 path components. Paths components will be separated by a <code>/</code>. All commands in the input are valid and will not refer to non-existent/invalid paths unless behavior is specified above. All commands will be less than 1024 characters.</p>

### 입력 

 <p>The first line of input contains <code>T</code> (<code>0 < T < 100</code>), indicating the number of test cases.</p>

<p>The next line of input contains <code>C</code> (<code>0 < C < 100</code>), indicating the number of commands for the test case. The next <code>C</code> lines will contain commands to generate the filesystem. The folder that the filesystem starts in may be ignored. In other words, the current directory (<code>./</code>) may be assumed.</p>

<p>The next line of input contains <code>Q</code> (<code>0 < Q < 20</code>), indicating the number of filenames for the test case whose contents should be printed. The next <code>Q</code> lines will contain filenames (or a path & filename, e.g. <code>myfolder/myfile</code>) to print out the contents of a given file.</p>

### 출력 

 <p>Output the contents of the file a query requests or "invalid!" if the file does not exist.</p>

<p>Print out a blank after each case.</p>

