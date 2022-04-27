# Tutorials

## [Creating Subplots in Matplotlib](https://python-course.eu/numerical-programming/creating-subplots-in-matplotlib.php)

```python
import matplotlib.pyplot as plt

python_course_green = "#476042"
fig = plt.figure(figsize=(6, 4))
sub1 = plt.subplot(2, 2, 1)
sub1.set_xticks(())
sub1.set_yticks(())
sub1.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center',
        size=20, alpha=.5)

sub2 = plt.subplot(2, 2, 2)
sub2.set_xticks(())
sub2.set_yticks(())
sub2.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center',
        size=20, alpha=.5)

sub3 = plt.subplot(2, 2, 3)
sub3.set_xticks(())
sub3.set_yticks(())
sub3.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center',
        size=20, alpha=.5)

sub4 = plt.subplot(2, 2, 4, facecolor=python_course_green)
sub4.set_xticks(())
sub4.set_yticks(())
sub4.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center',
        size=20, alpha=.5, color="y")

fig.tight_layout()
plt.show()
```

<p align="center">
  <a href="https://python-course.eu/numerical-programming/creating-subplots-in-matplotlib.php">
         <img src="https://user-images.githubusercontent.com/15319503/165600695-d58abf3e-082f-4732-930f-6ce2ff5c60c5.png" 
              width="450" height="300" alt="subplots-in-Python"/>
      </a>
</p>




