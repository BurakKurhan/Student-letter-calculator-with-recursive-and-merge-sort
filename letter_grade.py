__author__ = 'Burak.K'
#Ismail Burak Kurhan
#220201055

def read_from_file(): # This function's goal read from file to list
    grades_list=[]
    grades_list_txt=open('student_grades.txt','r')

    for i in grades_list_txt: #I used for loop for append every line in different lists
        i=i.split()
        i[2]=i[2].strip(";")
        i[3]=i[3].strip(";")
        i[0]=i[0].strip(":")
        grades_list.append(i)
    grades_list_txt.close()
    return grades_list



def calculate_average(grades_list):
    if len(grades_list)==0: # Base case for stop when lenght of grades_list ==0
        return grades_list
    else:
        total=0
        for i in range (len(grades_list[0])): # Average points founded by the given point rates
            if 1<= i <=2: # It calculate the first person every time
                total=(float(grades_list[0][i])*(1/5.0))+total
            elif i==3:
                total=(float(grades_list[0][i])*(2/5.0))+total
            elif i>3:
                total=(float(grades_list[0][i])*(1/20.0))+total
    grades_list[0].append(total)
    return  calculate_average(grades_list[1:]) # return with function with other persons for recursive


def finding_letter_grades(grades_list): # This function find letters
    if len(grades_list)==0: # It is base case
        return grades_list
    else:
        if 100 > grades_list[0][8] > 90: #Theese lines finds letters
            grades_list[0].append("AA")
            return finding_letter_grades(grades_list[1:])
        elif 89 > grades_list[0][8] > 85:
            grades_list[0].append("BA")
            return finding_letter_grades(grades_list[1:])
        elif 84 > grades_list[0][8] > 80:
            grades_list[0].append("BB")
            return finding_letter_grades(grades_list[1:])
        elif 80 > grades_list[0][8] > 75:
            grades_list[0].append("CB")
            return finding_letter_grades(grades_list[1:])
        elif 75 > grades_list[0][8] > 70:
            grades_list[0].append("CC")
            return finding_letter_grades(grades_list[1:])
        elif 69 > grades_list[0][8] > 65:
            grades_list[0].append("DC")
            return finding_letter_grades(grades_list[1:])
        elif 64 > grades_list[0][8] > 60:
            grades_list[0].append("DD")
            return finding_letter_grades(grades_list[1:])
        elif 59 > grades_list[0][8] > 50:
            grades_list[0].append("FD")
            return finding_letter_grades(grades_list[1:])
        elif 49 > grades_list[0][8] > 0:
            grades_list[0].append("FF")
            return finding_letter_grades(grades_list[1:])
        else:
            return finding_letter_grades(grades_list[1:]) #function run with other elements for recursion

def mergeSort(list): #This function sort list with Merge sort
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid] #Find mid and divide the list two half
        righthalf = list[mid:]

        mergeSort(lefthalf) #mergeSort function run with lefthalf and righthalf recursivly
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][8] > righthalf[j][8]: #if left one is bigger than right one list[k] equal to left one
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j] # else right one equal to list[k]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1



def write_to_file(list): # this function write the list to file
    writed_file=open("student_grades.txt","w") #opened for writing
    final_list=[]
    for i in range(len(list)):
        new_list=[]
        new_list.append(list[i][0]) #First append required elements to new_list
        new_list.append(list[i][8])
        new_list.append(list[i][9])
        final_list.append(new_list) #After, append it to final list
    for j in final_list:
        counter=0
        converted=""
        for m in j:
            if counter==0:
                converted=converted+str(m)+":" # I append ":" after the names
                counter+=1
            elif counter==1:
                converted=converted+str(m)+";" # append ";" after the averages
                counter+=1
            else:
                converted+= ' ' + str(m) # And also I convert string to write file
        writed_file.writelines(str(converted)+"\n")
#------------------Program starts here------------------
# Functions are called there
list=read_from_file()
calculate_average(list)
finding_letter_grades(list)
mergeSort(list)
write_to_file(list)