# -*- coding: utf-8 -*-


all_classes = [{"name_class": "4a", "scores": [1,0,0,0,0]},
            {"name_class": "11j", "scores": []},
            {"name_class": "6b", "scores": [1,3,4,2,2]},
            {"name_class": "10g", "scores": [2,3,3,1,4]}]

avarge_class_score_list = []

def get_avarge_class_score(name_class, scholar_scores):
    try:
        avarge_class_score = sum(scholar_scores)/len(scholar_scores)
    except (ZeroDivisionError):
        print ("The {} class is empty".format(name_class))
        return 0
    print ("{} avarge class scores = {}".format(name_class, avarge_class_score))
    return avarge_class_score


for school_class in iter(all_classes):
    avarge_class_score_list.append (get_avarge_class_score(school_class.get("name_class"),school_class.get("scores")))

avarge_class_score_list = [avarge_class_score for avarge_class_score in avarge_class_score_list if avarge_class_score != 0]

try:
    print ("Avarge school score = {}".format(sum(avarge_class_score_list)/len(avarge_class_score_list)))
except (ZeroDivisionError):
    exit("В школе нет учеников")