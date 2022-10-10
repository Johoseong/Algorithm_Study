import java.util.HashMap;
class Solution {
    public static String solution(String X, String Y) {
        String answer = "";
        HashMap<Integer, Integer> mapX = new HashMap<>();
        HashMap<Integer, Integer> mapY = new HashMap<>();
        String[] arrX = X.split("");
        String[] arrY = Y.split("");

        for (String x: arrX) {
            Integer tmp = Integer.parseInt(x);
            mapX.put(tmp, mapX.getOrDefault(tmp, 0) + 1);
        }
        for (String y: arrY) {
            Integer tmp = Integer.parseInt(y);
            mapY.put(tmp, mapY.getOrDefault(tmp, 0) + 1);
        }
        for (int i = 9; i >= 0; i--) {
            if (!mapX.containsKey(i) || !mapY.containsKey(i))
                continue;
            if (i == 0 && answer.isEmpty()) {
                answer = "0";
                break;
            }
            int min;
            if (mapX.get(i) < mapY.get(i))
                min = mapX.get(i);
            else
                min = mapY.get(i);
            answer += Integer.toString(i).repeat(min);
//            for (int j = 0; j < min; j++)
//                answer = answer + i;
        }
        if (answer.isEmpty())
            answer = "-1";
        return answer;
    }
}