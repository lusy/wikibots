import plotly
import plotly.plotly as py
import plotly.figure_factory as ff


df = [dict(Task="View related literature", Start='2018-08-15', Finish='2018-12-31'),
      dict(Task="Work on exposé feedback, finalise proposal", Start='2018-10-08', Finish='2018-10-31'),
      dict(Task="Finish literature review on methods", Start='2018-10-08', Finish='2018-10-31'),
      dict(Task="Propose own bot in front of the BAG", Start='2018-11-01', Finish='2018-11-21'),
      dict(Task="Gather bots", Start='2018-10-22', Finish='2018-10-31'),
      dict(Task="Identify bots with source code available", Start='2018-11-01', Finish='2018-11-07'),
      dict(Task="Select bots for case study", Start='2018-11-08', Finish='2018-11-20'),
      dict(Task="Code analysis", Start='2018-11-20', Finish='2019-01-31'),
      dict(Task="Check bot frameworks", Start='2018-11-20', Finish='2019-01-31'),
      dict(Task="Prepare interview questions", Start='2018-12-01', Finish='2018-12-15'),
      dict(Task="Reach out to bot developers", Start='2019-01-03', Finish='2019-01-03'),
      dict(Task="Conduct interviews with bot developers", Start='2019-01-04', Finish='2019-02-01'),
      dict(Task="Evaluate interviews", Start='2019-02-01', Finish='2019-02-20'),
      dict(Task="Formulate guidelines for ethical code", Start='2019-02-21', Finish='2019-02-28'),
      dict(Task="Register thesis", Start='2019-01-15', Finish='2019-01-15'),
      dict(Task="Write thesis", Start='2019-03-01', Finish='2019-05-31'),
      dict(Task="Proof-read", Start='2019-05-31', Finish='2019-06-15'),
      dict(Task="Submit thesis", Start='2019-06-15', Finish='2019-06-15')]

fig = ff.create_gantt(df, title='Timeline master thesis')
fig['layout']['margin'] = {'l': 250}
fig['layout']['width'] = 1200
plotly.offline.plot(fig, filename='gantt-thesis', auto_open=True)
