import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    class Date {
        int yy, mm, dd;
        
        public Date(String str) {
            String[] ss = str.split("\\.");
            this.yy = Integer.parseInt(ss[0]);
            this.mm = Integer.parseInt(ss[1]);
            this.dd = Integer.parseInt(ss[2]);
        }
    }
    
    int getTime(Date d) {
        return d.yy * 12 * 28 + d.mm * 28 + d.dd;
    }
    
    int countDay(Date start, Date end) {
        return getTime(end) - getTime(start);
    }

    public int[] solution(String today, String[] terms, String[] privacies) {
        HashMap<String, Integer> TERMS = new HashMap<>();
        for (String term: terms) {
            String[] ts = term.split(" ");
            TERMS.put(ts[0], Integer.parseInt(ts[1]));
        }

        Date todayDate = new Date(today);
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 0; i < privacies.length; i++) {
            String privacy = privacies[i];
            String[] ps = privacy.split(" ");
            Date date = new Date(ps[0]);
            int term = TERMS.get(ps[1]) * 28;
            if (countDay(date, todayDate) >= term) res.add(i+1);
        }
        
        return res.stream().mapToInt(i -> i).toArray();
    }
}