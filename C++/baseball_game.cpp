class Solution {
public:
    int calPoints(vector<string>& operations) {

        int n = operations.size();

        vector<int> record;
        // storing the scores of the baseball means!!

        for(int i = 0; i < n; i++){

            if(operations[i] != "D" && operations[i] != "C" && operations[i] != "+"){
            // stoi() function is used here in order to convert string to an integer
                record.push_back(stoi(operations[i]));
            }
            else if(operations[i] == "+"){
            // used record.size() here instead of the index(i) because the size of the array could be smaller than the index!!
                record.push_back(record[record.size()-1] + record[record.size()-2]);
            }
            else if(operations[i] == "C"){

                record.pop_back();
            }
            else if(operations[i] == "D"){

                record.push_back(2 * record[record.size()-1]);
            }
        }

        int sum = 0;

        for(int i = 0; i < record.size(); i++){

            sum += record[i];

        }
        return sum;
        
    }
};