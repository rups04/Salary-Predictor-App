From centos
RUN yum install python3 -y 
RUN pip3 install pandas scikit-learn
COPY dataset/* /home/
CMD python3 /home/model_train.py
