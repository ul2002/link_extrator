# Solution 1
sed 's|http[s]*://||g' domains.txt | sed 's|\.$||' | tr '[:upper:]' '[:lower:]' | awk -F. '{print $(NF-1)"."$NF}' | sort | uniq

# Solution 2
sed 's|http[s]*://||g; s|\.$||' domains.txt | tr '[:upper:]' '[:lower:]' | awk -F. '{if (NF>2) print $(NF-1)"."$NF; else print $0}' | sort | uniq

