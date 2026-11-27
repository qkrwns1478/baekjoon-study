import java.util.*;

public class Main {
	static Character[][] U, D, F, B, L, R;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while (T-- > 0) {
			initCube();
			int N = sc.nextInt();
			sc.nextLine();
			StringTokenizer st = new StringTokenizer(sc.nextLine());
			for (int i = 0; i < N; i++) {
				rotate(st.nextToken());
			}
			printArray(U);
		}
		sc.close();
	}
	
	static void initCube() {
		U = makeArray('w');
		D = makeArray('y');
		F = makeArray('r');
		B = makeArray('o');
		L = makeArray('g');
		R = makeArray('b');
	}
	
	static Character[][] makeArray(char c) {
		Character[][] res = new Character[3][3];
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				res[i][j] = c;
			}
		}
		return res;
	}
	
	static void printArray(Character[][] arr) {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(arr[i][j]);
			}
			System.out.println();
		}
	}
	
	static void rotate(String query) {
		char f = query.charAt(0);
		char d = query.charAt(1);
		boolean isClockwise = d == '+';
		
		// 1. 큐브 자체를 회전시켜 윗면을 기준으로 돌리도록 함
		switch (f) {
			case 'L': rotateCubeLR('R'); break;
			case 'R': rotateCubeLR('L'); break;
			case 'F': rotateCubeFB('B'); break;
			case 'B': rotateCubeFB('F'); break;
			case 'D': rotateCubeDown(); break;
		}
		
		// 2. 윗면을 기준으로 시계/반시계 방향으로 돌림
		rotateFace(U, isClockwise);
		Character[] tmp = new Character[3];
		for (int i = 0; i < 3; i++) {
			tmp[i] = !isClockwise ? R[0][i] : L[0][i];
		}
		for (int i = 0; i < 3; i++) {
			if (!isClockwise) R[0][i] = F[0][i];
			else			  L[0][i] = F[0][i];
		}
		for (int i = 0; i < 3; i++) {
			F[0][i] = !isClockwise ? L[0][i] : R[0][i];
		}
		for (int i = 0; i < 3; i++) {
			if (!isClockwise) L[0][i] = B[0][i];
			else			  R[0][i] = B[0][i];
		}
		for (int i = 0; i < 3; i++) {
			B[0][i] = tmp[i];
		}
		
		// 3. 큐브 자체를 회전시켜 원래 상태로 복구함
		switch (f) {
			case 'L': rotateCubeLR('L'); break;
			case 'R': rotateCubeLR('R'); break;
			case 'F': rotateCubeFB('F'); break;
			case 'B': rotateCubeFB('B'); break;
			case 'D': rotateCubeDown(); break;
		}
	}
	
	static void rotateFace(Character[][] arr, boolean isClockwise) {
		Character[][] tmp = new Character[3][3];
		int cnt = isClockwise ? 1 : 3;
		for (int k = 0; k < cnt; k++) {
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					tmp[j][2-i] = arr[i][j];
				}
			}
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					arr[i][j] = tmp[i][j];
				}
			}
		}
	}
	
	static void rotateCubeLR(char f) {
		boolean isLeft = f == 'L';
		Character[][] tmp = new Character[3][3];
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				tmp[i][j] = isLeft ? L[i][j] : R[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (isLeft) L[i][j] = U[i][j];
				else		R[i][j] = U[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				U[i][j] = isLeft ? R[i][j] : L[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (isLeft) R[i][j] = D[i][j];
				else		L[i][j] = D[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				D[i][j] = tmp[i][j];
			}
		}
		
		rotateFace(U, !isLeft);
		rotateFace(D, !isLeft);
		rotateFace(L, !isLeft);
		rotateFace(R, !isLeft);
		rotateFace(F, !isLeft);
		rotateFace(B, isLeft);
	}
	
	static void rotateCubeFB(char f) {
		boolean isFront = f == 'F';
		Character[][] tmp = new Character[3][3];
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				tmp[i][j] = isFront ? F[i][j] : B[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (isFront) F[i][j] = U[i][j];
				else		 B[i][j] = U[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				U[i][j] = isFront ? B[i][j] : F[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (isFront) B[i][j] = D[i][j];
				else		 F[i][j] = D[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				D[i][j] = tmp[i][j];
			}
		}
		
		rotateFace(R, !isFront);
		rotateFace(L, isFront);
		for (int i = 0; i < 2; i++) {
			rotateFace(B, true);
			rotateFace(isFront ? U : D, true);
		}
	}
	
	static void rotateCubeDown() {
		Character[][] tmp = new Character[3][3];
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				tmp[i][j] = D[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				D[i][j] = U[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				U[i][j] = tmp[i][j];
			}
		}
		
		tmp = new Character[3][3];
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				tmp[i][j] = F[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				F[i][j] = B[i][j];
			}
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				B[i][j] = tmp[i][j];
			}
		}
		
		for (int i = 0; i < 2; i++) {
			rotateFace(F, true);
			rotateFace(B, true);
			rotateFace(L, true);
			rotateFace(R, true);
		}
	}
}
