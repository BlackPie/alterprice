gulp = require 'gulp'
gutil = require 'gulp-util'
watchify = require 'watchify'
browserify = require 'browserify'
assign = require 'lodash.assign'
buffer = require 'vinyl-buffer'
source = require 'vinyl-source-stream'
rename = require 'gulp-rename'
plugins = require('gulp-load-plugins')()
less = require 'gulp-less'
consolidate = require 'gulp-consolidate'
minifyCss = require 'gulp-minify-css'
uglify = require 'gulp-uglify'
gbower = require 'gulp-bower'
spritesmith = require 'gulp.spritesmith'


ASSETS_SRC = "src/assets/src/"
ASSETS_DIST = "src/assets/dist/"


customOpts = {
    entries: ['./src/assets/src/coffee/main.coffee']
    debug: true
    transform: ['coffeeify']
    extensions: ['.coffee']
    paths: [
        './node_modules'
        "#{ASSETS_SRC}/coffee"
    ]
}

opts = assign {}, watchify.args, customOpts
b = watchify browserify(opts)


bundle = ->
    return b.bundle()
        .on 'error', gutil.log.bind(gutil, 'Browserify Error')
        .pipe source('bundle.js')
        .pipe buffer()
        .pipe rename('main.js')
        #.pipe uglify()
        .pipe gulp.dest(ASSETS_DIST + 'js')


gulp.task 'scripts', bundle
b.on 'update', bundle
b.on 'log', gutil.log


onError = (err) ->
    gutil.beep()
    gutil.log gutil.colors.red('Error caught:'), err
    if process.env.IGNORE_ERROR
        gutil.log gutil.colors.red('Ignore error: keep going')
    else
        gutil.log gutil.colors.red('Terminated')
        process.exit -1

# build scripts for production
gulp.task 'build_scripts', ['bower'], ->
    browserify(customOpts).bundle()
        .on 'error', gutil.log.bind(gutil, 'Browserify Error')
        .pipe source('bundle.js')
        .pipe buffer()
        .pipe rename('main.js')
        .pipe gulp.dest(ASSETS_DIST + 'js')

gulp.task 'bower', ->
    gbower()
        .pipe(gulp.dest('lib/'))

gulp.task 'less', ->
    gulp.src "#{ASSETS_SRC}less/main.less"
        .pipe(plugins.plumber({errorHandler: onError}))
        .pipe less()
        .pipe(minifyCss())
        .pipe gulp.dest "#{ASSETS_DIST}css/"


gulp.task 'watch', ->
  gulp.watch "#{ASSETS_SRC}less/**/*.less", ->
    gulp.run('less')

  gulp.watch "#{ASSETS_SRC}coffee/**/*.coffee", ->
    gulp.run('scripts')


gulp.task 'sprite', ->
    spriteData = gulp.src("#{ASSETS_SRC}images/sprites/1x/*.png").pipe(spritesmith
        imgName: 'sprite.png'
        cssName: 'sprite.less'
        imgPath: "../../src/images/sprite.png"
    )
    spriteData.img.pipe gulp.dest("#{ASSETS_SRC}images/")
    spriteData.css.pipe gulp.dest("#{ASSETS_SRC}less/utils/")

    spriteData2x = gulp.src("#{ASSETS_SRC}images/sprites/2x/*.png").pipe(spritesmith
        imgName: 'sprite_2x.png'
        cssName: 'sprite_2x.less'
        imgPath: "../../src/images/sprite_2x.png"
    )
    spriteData2x.img.pipe gulp.dest("#{ASSETS_SRC}images/")
    spriteData2x.css.pipe gulp.dest("#{ASSETS_SRC}less/utils/")


gulp.task 'default', ['scripts', 'less', 'watch']
gulp.task 'build', ['build_scripts', 'less']
