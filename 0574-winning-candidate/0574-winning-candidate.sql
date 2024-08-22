# Write your MySQL query statement below


select c.name from Candidate as c join 
(select candidateId, count(*) as vote_count
from vote
group by candidateId
order by count(*) desc
limit 1) as v on c.id = v.candidateId;
