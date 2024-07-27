export default function getStudentIdsSum(arr) {
  return Array.isArray(arr) ? arr.reduce((sum, curr) => sum + curr.id, 0) : 0;
}
