import java.util.HashMap;

class Solution {
    public static String solution(String X, String Y) {
        StringBuilder answer = new StringBuilder();
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
            if (i == 0 && "".equals(answer.toString()))
                return "0";

            answer.append(Integer.toString(i).repeat(Math.min(mapX.get(i), mapY.get(i))));
        }
        if ("".equals(answer.toString()))
            return "-1";
        return answer.toString();
    }

}