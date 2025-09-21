import java.util.*;

class MovieRentingSystem {

    private Map<Integer, TreeSet<int[]>> unrented;
    private Map<ShopMovieKey, Integer> prices;
    private TreeSet<int[]> rented;

    public MovieRentingSystem(int n, int[][] entries) {
        unrented = new HashMap<>();
        prices = new HashMap<>();
        
        rented = new TreeSet<>((a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            if (a[1] != b[1]) return a[1] - b[1];
            return a[2] - b[2];
        });

        for (int[] entry : entries) {
            int shop = entry[0];
            int movie = entry[1];
            int price = entry[2];

            prices.put(new ShopMovieKey(shop, movie), price);

            unrented.putIfAbsent(movie, new TreeSet<>((a, b) -> {
                if (a[0] != b[0]) return a[0] - b[0];
                return a[1] - b[1];
            }));
            unrented.get(movie).add(new int[]{price, shop});
        }
    }
    
    public List<Integer> search(int movie) {
        List<Integer> result = new ArrayList<>();
        if (!unrented.containsKey(movie)) {
            return result;
        }

        int count = 0;
        for (int[] p : unrented.get(movie)) {
            result.add(p[1]);
            count++;
            if (count == 5) {
                break;
            }
        }
        return result;
    }
    
    public void rent(int shop, int movie) {
        int price = prices.get(new ShopMovieKey(shop, movie));
        unrented.get(movie).remove(new int[]{price, shop});
        rented.add(new int[]{price, shop, movie});
    }
    
    public void drop(int shop, int movie) {
        int price = prices.get(new ShopMovieKey(shop, movie));
        rented.remove(new int[]{price, shop, movie});
        unrented.get(movie).add(new int[]{price, shop});
    }
    
    public List<List<Integer>> report() {
        List<List<Integer>> result = new ArrayList<>();
        int count = 0;
        for (int[] r : rented) {
            result.add(Arrays.asList(r[1], r[2]));
            count++;
            if (count == 5) {
                break;
            }
        }
        return result;
    }

    private static class ShopMovieKey {
        private final int shop;
        private final int movie;

        public ShopMovieKey(int shop, int movie) {
            this.shop = shop;
            this.movie = movie;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            ShopMovieKey that = (ShopMovieKey) o;
            return shop == that.shop && movie == that.movie;
        }

        @Override
        public int hashCode() {
            return Objects.hash(shop, movie);
        }
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = new MovieRentingSystem(n, entries);
 * List<Integer> param_1 = obj.search(movie);
 * obj.rent(shop,movie);
 * obj.drop(shop,movie);
 * List<List<Integer>> param_4 = obj.report();
 */