const gulp = require('gulp');
const bs = require('browser-sync');
const exec = require('child_process').exec;

gulp.task('runserver', () => {
    let proc = exec('python app.py');
});

gulp.task('browser-sync', ['runserver'], () => {
    bs({
        notify: true,
        proxy: 'localhost:5000'
    })
});

gulp.task('watch', () => {
    gulp.watch(['**/*.html',
                '**/*.js',
                '**/*.css'])
        .on('change', bs.reload);
});

gulp.task('default', ['watch', 'browser-sync'])